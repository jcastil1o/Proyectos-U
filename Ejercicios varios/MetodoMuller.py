def muller_method(f, x0, x1, x2, tol=1e-6):
  """
  Implementación del método de Muller para encontrar la raíz de una función.

  Parámetros:
      f: La función cuya raíz se desea encontrar.
      x0, x1, x2: Tres puntos iniciales.
      tol: Tolerancia de convergencia.

  Devuelve:
      La raíz aproximada de la función.
  """
  iteration = 0
  while True:
    iteration += 1
    h0 = x1 - x0
    h1 = x2 - x1
    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)

    # Check for zero denominator before calculating c3
    if abs(h1 - h0) < tol:
      raise ZeroDivisionError("h1 and h0 are too close together. Try different initial points.")

    c2 = (h1 - h0) / (f1 - f0 - f2)
    c3 = (f1 - f0) / (h1 - h0)

    h2 = c2 * f2 / (c2 + c3)

    if abs(h2) < tol:
      print(f"Iteración {iteration}: Raíz aproximada: {x2}")
      return x2

    x3 = x2 - h2

    x0 = x1
    x1 = x2
    x2 = x3

