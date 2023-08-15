// Función para calcular la proporción entre dos números
function calcularProporcion(a, b) {
  return a / b;
}

// Función para verificar si una proporción cumple con la Proporción Dorada
function cumpleProporcionDorada(proporcion) {
  const proporcionDorada = 1.61803398875;
  const margenTolerancia = 0.01;

  return Math.abs(proporcion - proporcionDorada) < margenTolerancia;
}

// Función para recorrer el DOM y verificar proporciones
function recorrerDOMyVerificarProporciones(elemento) {
  const elementosHijos = elemento.children;
  let totalProporciones = 0;
  let totalElementos = 0;

  for (let i = 0; i < elementosHijos.length; i++) {
    const hijo = elementosHijos[i];
    const ancho = hijo.offsetWidth;
    const alto = hijo.offsetHeight;
    const proporcion = calcularProporcion(ancho, alto);

    if (cumpleProporcionDorada(proporcion)) {
      totalProporciones += proporcion;
    }
    totalElementos++;

    // Recorre los elementos hijos de forma recursiva
    recorrerDOMyVerificarProporciones(hijo);
  }

  return { totalProporciones, totalElementos };
}

// Espera a que el DOM esté completamente cargado no anda si lo pones en la consolq
document.addEventListener("DOMContentLoaded", function() {
  // Comienza a recorrer el DOM desde el elemento raíz (body)
  const resultado = recorrerDOMyVerificarProporciones(document.body);
  const promedio = resultado.totalProporciones / resultado.totalElementos;
  console.log(`Promedio de todas las proporciones: ${promedio}`);
});

// Llamada inicial a recorrerDOMyVerificarProporciones después de un retraso
setTimeout(function() {
  // Comienza a recorrer el DOM desde el elemento raíz (body)
  recorrerDOMyVerificarProporciones(document.body);
}, 30);
