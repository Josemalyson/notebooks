# Assignment

I often need "fake data" to show people how to do data manipulation tasks with regular expressions or pandas. The
problem is that sometimes the data I generate on the web is too messy, and I get bogged down showing students how to
clean all of the data when some of it isn't representative of what I want. In this assignment you get a chance to help
me generate realistic fake data, all with llama 2!

For each question I will describe the data in natural language and you must write a function which queries llama 2 to
generate data in that format and adhere to the description I've written.


## Question 1

Generate for me a list of ten fictitious names, where the first name is a single word, and the last (family) name may be
(but doesn't have to be!) up to two words separated by a hyphen. Don't include titles, honorifics, or middle names. The
autograder will expect that you return a list[str] where each value in the list is a full name.

import os
import json
import re
from llama_cpp import Llama
from llama_cpp.llama_types import *
from llama_cpp.llama_grammar import *
from dataclasses import dataclass

def generate_names() -> list[str]:
    results: list[str] = []

    model: Llama = Llama(model_path=os.environ["LLAMA_13B"], verbose=False, n_ctx=2048)

    prompt = '''Generate 10 fictitious names in JSON where the first name is a single word, and the last (family) name may be
    (but doesn't have to be!) up to two words separated by a hyphen. Don't include titles, honorifics, or middle names. The
    autograder will expect that you return a list[str] where each value in the list is a full name.

    Generate 10 fictitious names in JSON:
    [{"firstName":"Jasper","lastName":"Stonehart"},{"firstName":"Sienna","lastName":"Brightvale"},{"firstName":"Ronan","lastName":"Cloudrunner"},{"firstName":"Violet","lastName":"Dewdrop"},{"firstName":"Kai","lastName":"Thornfield"},{"firstName":"Elara","lastName":"Moonshadow"},{"firstName":"Finn","lastName":"Waverly"},{"firstName":"Luna","lastName":"Starwhisper"},{"firstName":"Orion","lastName":"Frostfire"},{"firstName":"Cora","lastName":"Silverstream"}]

    Generate 10 fictitious names in JSON:
    '''  

    results_prompt = model.create_completion(
        prompt=prompt,
        stream=False, 
        max_tokens=2048,
        temperature=0.8,
    )

    # Extract the text response
    response_text = results_prompt["choices"][0]["text"].strip()  # Trim whitespace

    # Use regex to find valid JSON list in the response
    json_match = re.search(r'(\[.*?\])', response_text, re.DOTALL)
    if json_match:
        json_data = json_match.group(1)
        results = json.loads(json_data)
    else:
        raise ValueError("No valid JSON found in the response.")

    return results[:10]

# Invoke student code

from contextlib import redirect_stderr
import tempfile

with redirect_stderr( tempfile.TemporaryFile('wt') ) as error_catcher:
    results = generate_names()
    print(results)

# Verify the length
assert (
    len(results) == 10
), f"You did not return ten and only ten results, instead we got {len(results)}."

## Question 2

Generate for me a list of 5 things to do in your hometown (or mine if you prefer, Ann Arbor Michigan!). The key is that
these should all (a) start with a number and (b) be no more than three sentences long. So the following would be a good
item:

- 1\. Go to the Henry Ford Museum. The Henry Ford Museum has all sorts of wonderful exhibits for all ages. One
  particular highlight includes giants trains!

While the following would **not be good items** (the first item does not start a numbered list, the second item is not a
sentence as it doesn't end in punctuation, and the third item just goes on and on and on):

- A\. Go to the University of Michigan. The University of Michigan is a school with more than 50,000 students in Ann
  Arbor, MI. The University of Michigan is a public School.
- 2\. Visit the Detroit Eastern Market
- 3\. Visit Sleeping Bear Dunes. The dunes are located along the northwest coast of the Lower Peninsula of Michigan in
  Leelanau and Benzie counties near Traverse City. It covers a 35-mile-long stretch of Lake Michigan's eastern
  coastline, as well as North and South Manitou islands. This national park is known for its massive dunes, some of
  which are over 400 feet high. The area gets its name from the Native American legend of the Sleeping Bear. According
  to the story, a mother bear and her two cubs were trying to cross Lake Michigan from Wisconsin to escape a forest
  fire.

import os
import json
import re
from llama_cpp import Llama
from llama_cpp.llama_types import *
from llama_cpp.llama_grammar import *
from dataclasses import dataclass

def generate_trip_recommendations() -> list[str]:
    results: list[str] = []

    model: Llama = Llama(model_path=os.environ["LLAMA_13B"], verbose=True, n_ctx=2048)

    prompt = '''Generate a list of 5 things to do in Michigan in JSON:    
    [{"activity":"1. Visit the University of Michigan","description":"Explore the beautiful campus and its impressive architecture. Don't miss the Law Quadrangle and the iconic Diag."},{"activity":"2. Stroll through the Matthaei Botanical Gardens","description":"Enjoy the lush gardens and trails that showcase a variety of plant species. The conservatory is a perfect spot for a peaceful escape."},{"activity":"3. Check out the Ann Arbor Hands-On Museum","description":"Ideal for families, this interactive museum offers fun exhibits that engage visitors of all ages. It’s a great way to spark curiosity and learning."},{"activity":"4. Attend a performance at the Michigan Theater","description":"Catch a movie or live performance in this historic venue known for its stunning interior. It’s a cultural gem in the heart of downtown."},{"activity":"5. Explore the Kerrytown District","description":"Discover unique shops, eateries, and the famous Ann Arbor Farmers Market. This vibrant area is perfect for a leisurely afternoon."}]

    Generate a list of 5 things to do in Michigan in JSON: 
    '''

    results_prompt = model.create_completion(
        prompt=prompt,
        stream=False, 
        max_tokens=2048,
        temperature=0.8,
    )

    # Extract the text response
    response_text = results_prompt["choices"][0]["text"].strip()  # Trim whitespace

    # Use regex to find valid JSON list in the response

    json_match = re.search(r'(\[.*?\])', response_text, re.DOTALL)
    if json_match:
        json_data = json_match.group(1)
        results = json.loads(json_data)
    else:
        raise ValueError("No valid JSON found in the response.")

    return  results[:5]

# Invoke student code
from contextlib import redirect_stderr
import re
import tempfile

with redirect_stderr( tempfile.TemporaryFile('wt') ) as error_catcher:
    results=generate_trip_recommendations()
    print(results)

# Verify length
assert (
    len(results) == 5
), f"You did not return five and only five results, instead we got {len(results)}."

## Question 3

Generate for me US-based addresses which have a person's name which usually appears on the first line, an optional
company name which often goes on the second line, a street address which has a number followed by some text description,
a city and state where the state is a two letter identifier and comes after the city name, and zip code which is a five
digit number (but as a string, since it could start with 0) followed by an optional hyphen and four more digits.


To make it easy for you to conform to this set of requirements, I created a simple class from the following example --
my mailing address!

> Dr. Christopher Brooks
>
> > School of Information, University of Michigan
> >
> > 105 S. State St.
> >
> > Ann Arbor, MI
> >
> > 48109-1285

Your function should return exactly 5 of these entries!

And, if you've gotten this far in the course, why not send me a postcard and introduce yourself? Everyone loves getting
mail!

(Don't forget to add **United States** if sending mail internationally, even though field is missing from the assignment
`MailingAddress` class.)

import os
import json
import re
from llama_cpp import Llama
from llama_cpp.llama_types import *
from llama_cpp.llama_grammar import *
from dataclasses import dataclass

@dataclass
class MailingAddress:
    name: str
    business_name: str
    street_number: int
    street_text: str
    city: str
    state: str
    zip_code_short: str
    zip_code_long: str
    country: str

def generate_addresses() -> list[MailingAddress]:
    results: list[MailingAddress] = []

    model: Llama = Llama(model_path=os.environ["LLAMA_13B"], verbose=False, n_ctx=2048)

    prompt = '''Generate a list of 5 mailing addresses in JSON format U.S.-based mailing addresses in JSON format. Each address should include:
    - A person's name on the first line.
    - An optional company name on the second line.
    - A street address consisting of a number followed by text description.
    - A city followed by a two-letter state identifier.
    - A zip code as a five-digit string, which may include a hyphen and four additional digits.

    Generate a list of 5 mailing addresses in JSON format:
    [{"name":"Dr. Christopher Brooks","business_name":"School of Information, University of Michigan","street_number":105,"street_text":"S. State St.","city":"Ann Arbor","state":"MI","zip_code_short":"48109","zip_code_long":"48109-1285","country":"United States"},{"name":"Prof. Sarah Johnson","business_name":"Department of Biology, University of Michigan","street_number":200,"street_text":"E. University Ave.","city":"Ann Arbor","state":"MI","zip_code_short":"48109","zip_code_long":"48109-1205","country":"United States"},{"name":"Dr. Emily Tran","business_name":"College of Engineering, University of Michigan","street_number":150,"street_text":"N. Ingalls St.","city":"Ann Arbor","state":"MI","zip_code_short":"48109","zip_code_long":"48109-2006","country":"United States"}]

    Generate a list of 5 mailing addresses in JSON format:
    '''

    results_prompt = model.create_completion(
        prompt=prompt,
        stream=False, 
        max_tokens=2048,
        temperature=0.8,
    )

    response_text = results_prompt["choices"][0]["text"].strip()  # Trim whitespace

    # Use regex to find valid JSON list in the response

    json_match = re.search(r'(\[.*?\])', response_text, re.DOTALL)
    if json_match:
        json_data = json_match.group(1)
        results = json.loads(json_data)
    else:
        raise ValueError("No valid JSON found in the response.")

    return  results[:5]

# Invoke student code

from contextlib import redirect_stderr
import tempfile

with redirect_stderr( tempfile.TemporaryFile('wt') ) as error_catcher:
    results=generate_addresses()
    print(results)

# Verify length
assert (
    len(results) == 5
), f"You did not return five and only five results, instead we got {len(results)}."
