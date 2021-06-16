def CodelandUsernameValidation(username):
  # Obtengo la longitud del nombre de usuario
  longitud_username = len(username)

  # Si la longitud está entre 4 y 25
  if longitud_username >= 4 and longitud_username <= 25:
    # Si el nombre de usuario inicia con letras
    if username[0].isalpha():
      # Si la cadena solo contiene letras, números, y guiones bajo
      if username.isalnum() or "_" in username:
        # Si el nombre de usuario NO termina en guion bajo
        if username[-1] != "_":
          return 'true'
        else:
          return 'false'
      else:
        return 'false'
    else:
      return 'false'
  else:
    return 'false'