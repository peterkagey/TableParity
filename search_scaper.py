import urllib.request
import urllib.parse
import json
import time

class SearchScraper:
    def __init__(self, search_terms):
        self.search_terms = search_terms

    def search_url(self, page):
      # https://oeis.org/search?q=keyword%3atabl%20author%3akagey&fmt=json
        uri = "https://oeis.org/search?q=" + urllib.parse.quote(self.search_terms) + "&fmt=json" + "&start=" + str(page*10)
        # print(uri)
        return uri

    def search_json(self, page=0):
        fp = urllib.request.urlopen(self.search_url(page))
        response_bytes = fp.read()
        response_text = response_bytes.decode("utf8")
        fp.close()
        return json.loads(response_text)

    def sequence_list(self, json_data):
      sequences = []
      # print(json_data)
      if json_data["count"] == 0:
        return []
      for seq_data in json_data["results"]:
        sequences.append(seq_data["number"])
      return list(map(lambda i: "A" + str(i).zfill(6), sequences))

    def all_sequences(self):
      first_page_results = self.search_json()
      page_count = first_page_results["count"]//10
      print(str(page_count) + " pages:")
      sequences = self.sequence_list(first_page_results)
      for i in range(page_count):
        print(i+1,"of",page_count)
        json = self.search_json(i + 1)
        sequences_on_page = self.sequence_list(json)
        print(sequences_on_page)
        sequences += sequences_on_page
        time.sleep(5) # Throttle requests so that the OEIS servers aren't hit too hard.
      return sequences

search_term = "keyword:tabl link:flattened link:200"
print("Search terms: ", s)
scraper = SearchScraper(s)
print(scraper.all_sequences())

