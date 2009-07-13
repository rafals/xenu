def tag(tag, *args, **kwargs):
  """funkcja bazowa dla wszystkich tagow html"""
  
  attributes = {}
  contents = []
  
  # porzadkowanie danych wejsciowych
  # pobranie atrybutow z hasha jako 1. argumentu
  if len(args) and isinstance(args[0], dict):
    attributes = args[0]
  # zawartosc
    contents = args[1:]
  else:
    contents = args
  # pobranie z keyword-argumentow (w razie konfliktow z hashem wygrywaja keywordy)
  if len(kwargs):
    for k in kwargs:
      attributes[k] = kwargs[k]
  
  # generowanie htmla
  result = "<" + tag
  # z argumentow
  if len(attributes):
    result += " " + " ".join([k + '="' + attributes[k] + '"' for k in attributes])
  
  def tab(html):
    """robienie wciec"""
    return "\n".join(map(lambda line: "  " + line, html.split("\n")))
  
  # z zawartosci  
  if len(contents):
    result += ">\n" + tab("\n".join(["\n".join(c) if isinstance(c, tuple) or isinstance(c, list) else str(c) for c in contents]))
    result += "\n</" + tag + ">"
  else:
    result += "/>"  
  return result

def create_tag(t):
  """tworzenie nowej funkcji-taga"""
  def new_tag(*args, **kwargs):
    return tag(t, *args, **kwargs)
  return new_tag

tags = ['html', 'head', 'title', 'script', 'link', 'body', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'div', 'span',
        'img', 'br', 'hr', 'a', 'ul', 'li']

# umieszczenie w globalsach funkcji dla kazdego taga
for t in tags:
  globals()[t] = create_tag(t)