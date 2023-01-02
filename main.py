import json
import sys
import requests as req

URL = "https://api.kampusmerdeka.kemdikbud.go.id/magang/browse/position"
FETCH_COUNT = 100

def get_url_for_id(id: str) -> str:
  return f"{URL}/{id}"

def get_url_fetch(offset: int, limit: int) -> str:
  return f"{URL}?offset={offset}&limit={limit}"

def main(argv: list[str]) -> int:
  fp = open("result.txt", "w")
  item_counter = 1
  counter = 0

  while True:
    response = req.get(get_url_fetch(counter, FETCH_COUNT))
    counter += FETCH_COUNT

    response_content_str = response.content.decode()
    
    if response.status_code != 200:
      raise Exception(f"Error occurred: {response_content_str}")

    response_json = json.loads(response_content_str)

    items = response_json["data"]
    if len(items) == 0:
      break

    for item in items:
      if item["activity_type"] == "BLENDED":
        print(item_counter, "\t", item["name"], file=fp)
        print("\t\t", item["mitra_name"], file=fp)
        print("\t\t", item["activity_name"], file=fp)
        print("\t\t", get_url_for_id(item["id"]), file=fp)
        item_counter += 1
  return 0

if __name__ == "__main__":
  sys.exit(main(sys.argv))
