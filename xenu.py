def base_tag(tag, *args, **kwargs):
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

def tag(t):
  """tworzenie nowej funkcji-taga"""
  def new_tag(*args, **kwargs):
    return base_tag(t, *args, **kwargs)
  return new_tag

# all HTML 4 and HTML 5 tags from http://www.w3schools.com/tags/html5.asp
all_tags = ['a', 'abbr', 'acronym', 'address', 'applet', 'area', 'article', 'aside', 'audio', 'b', 'base',
        'basefont', 'bdo', 'big', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'center', 'cite',
        'code', 'col', 'colgroup', 'command', 'datagrid', 'datalist', 'datetemplate', 'dd', 'details',
        'dialog', 'dfn', 'dir', 'div', 'dl', 'dt', 'em', 'embed', 'event-source', 'fieldset', 'figure', 'font',
        'footer', 'form', 'frame', 'frameset', 'head', 'header', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr',
        'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'label', 'legend', 'li', 'link', 'm', 'map',
        'menu', 'meta', 'meter', 'nav', 'nest', 'noframes', 'noscript', 'oject', 'ol', 'optgroup', 'option',
        'p', 'param', 'pre', 'progress', 'q', 'rule', 's', 'samp', 'script', 'section', 'select', 'small',
        'source', 'span', 'strike', 'strong', 'style', 'sub', 'sup', 'table', 'tbody', 'td', 'textarea',
        'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'tt', 'u', 'ul', 'var', 'video']

popular_tags = ['html', 'head', 'body', 'title', 'meta', 'script', 'link', 'body', 'span', 'p', 'div', 'ul',
        'ol', 'li', 'h1', 'h2', 'h3', 'hr', 'br', 'img', 'a', 'pre', 'blockquote', 'button', 'form', 'input',
        'label', 'legend', 'fieldset', 'select', 'option']

tags = popular_tags

# umieszczenie w globalsach funkcji dla kazdego taga
for t in tags:
  globals()[t] = tag(t)