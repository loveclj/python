# __author__ = 'lizhifeng'
import urllib
import urllib2
import json
import time


def split_cnt(limit, divide):
    _cnt_list = []
    while limit > 0:
        limit -= divide
        if limit >= 0:
            _cnt_list.append(divide)
        else:
            _cnt_list.append(limit + divide)
    return _cnt_list

def request_solr_retry(url, pid_pn, max_retry=5):
    retry = 0
    while retry < max_retry:
        try:
            start = time.time()
            _content_str = urllib2.urlopen(url).read()
            print "reqest ", time.time() - start
            # print _content_str
            start = time.time()
            _content_json = json.loads(_content_str)
            _next_cursor_mark = _content_json["nextCursorMark"]

            _docs = _content_json["response"]["docs"]
            for _doc in _docs:
                pn = _doc["PN_STR"]
                pid = _doc["_id"]
                pid_pn[pid] = pn
            print "json parse ", time.time() - start

            return _next_cursor_mark

        except:
            print "retry"
            retry += 1
            continue

    return ""


class SearchSolr:
    def __init__(self):
        self.limit = 1000
        self.cnt_max = 200
        self.solr_host = "192.168.3.248"
        self.solr_port = 9088
        self.query = u"car"
        self.query_cnt_list = []
        self.query_append = ",UniqueKey%20desc"

    def adapt_query(self, query):
        if query.find(self.query_append) != -1:
            return query

        if query.find("sort=") == -1:
            query += u"&sort=score%20desc,_version_%20desc,UniqueKey%20desc"
            return query

        index = query.find(u"&")
        if index == -1:
            query += self.query_append
            return query
        else:
            query = query[0:index] + self.query_append + query[index:-1]
            return query

    def set_query_url(self, query, rows, cursor_mark):
        cursor_mark_encoded = urllib.quote(cursor_mark)
        # print cursor_mark_encoded

        url = u"http://"
        url += self.solr_host
        url += u":"
        url += str(self.solr_port)
        url += u"/patsnap/PATENT/EN_CN?fl=_id,PN_STR&q="
        url += query
        url += u"&wt=json&timeAllowed=0&rows="
        url += str(rows)
        url += u"&cursorMark="
        url += cursor_mark_encoded

        return url

    def get_pid_pn(self):
        self.query_cnt_list = split_cnt(self.limit, self.cnt_max)
        next_cursor_mark = "*"
        pid_pn ={}
        for row in self.query_cnt_list:
            query = self.adapt_query(self.query)
            url = self.set_query_url(query, row, next_cursor_mark)
            next_cursor_mark = request_solr_retry(url, pid_pn)

        return pid_pn

    def test(self):
        start = time.time()
        pid_pn = self.get_pid_pn()
        print time.time() - start

        for pid, pn in pid_pn.items():
            print pid + " " + pn


if __name__ == "__main__":
    p = SearchSolr()
    p.test()




