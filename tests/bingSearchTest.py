from app.bingSearch import search
## unittest - Bing Search function test
bing_results = search("peanuts", 4)
print "Search has", len(bing_results), "results"