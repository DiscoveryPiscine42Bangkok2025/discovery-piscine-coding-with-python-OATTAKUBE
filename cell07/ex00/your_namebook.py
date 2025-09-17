def array_of_names(s : dict) -> list:
  full_name = []
  for first , last in s.items() :
    name = first.capitalize() + " " + last.capitalize()
    full_name.append(name)
  return full_name

person = {
  "jean": "valjean",
  "grace": "hopper",
  "xavier": "niel",
  "fifi": "brindacier"
}    

print(array_of_names(person))
