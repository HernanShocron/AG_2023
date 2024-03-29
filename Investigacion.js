// Función para calcular la proporción entre dos números
function calcularProporcion(a, b) {
  if(a>b){ return a / b}
  else  {return b / a}
}

// Función para verificar si una proporción cumple con la Proporción Dorada
function cumpleProporcionDorada(proporcion) {
  const proporcionDorada = 1.61803398875;
  const margenTolerancia = 0.1;

  return Math.abs(proporcion - proporcionDorada) < margenTolerancia;
}

// Función para recorrer el DOM y calcular todas las proporciones
function recorrerDOMyCalcularProporciones(elemento) {
  const elementosHijos = elemento.children;
  let proporciones = [];
  let proporcionesDoradas = [];

  for (let i = 0; i < elementosHijos.length; i++) {
    const hijo = elementosHijos[i];
    const ancho = hijo.offsetWidth;
    const alto = hijo.offsetHeight;
    const proporcion = calcularProporcion(ancho, alto);

    // Verifica si la proporcion es un número y no es infinita antes de agregarla
    if (!isNaN(proporcion) && isFinite(proporcion)) {
      proporciones.push(proporcion);
    }

    if (cumpleProporcionDorada(proporcion)) {
      proporcionesDoradas.push(proporcion);
      elemento.style.backgroundColor = "red";
    }

    // Recorre los elementos hijos de forma recursiva
    const { proporciones: subProporciones, proporcionesDoradas: subProporcionesDoradas } = recorrerDOMyCalcularProporciones(hijo);
    proporciones = proporciones.concat(subProporciones);
    proporcionesDoradas = proporcionesDoradas.concat(subProporcionesDoradas);
  }

  return { proporciones, proporcionesDoradas };
}
// Función para calcular el error entre el promedio total y la Proporción Dorada
function calcularErrorPromedio(proporciones) {
  const proporcionDorada = 1.61803398875;
  const sumaProporciones = proporciones.reduce((total, proporcion) => total + proporcion, 0);
  const promedioTotal = sumaProporciones / proporciones.length;
  const error = Math.abs(promedioTotal - proporcionDorada);
  return error;
}
// Función para calcular y mostrar los promedios
function calcularYMostrarPromedios() {
  const { proporciones, proporcionesDoradas } = recorrerDOMyCalcularProporciones(document.body);
  const longitudProporciones = proporciones.length;
  const longitudProporcionesDoradas = proporcionesDoradas.length;
  if (proporciones.length === 0) {
    console.log("No se encontraron proporciones en el DOM.");
  } else {
    const errorPromedioTotal = calcularErrorPromedio(proporciones);
    console.log(`Error con respecto a la Proporción Dorada: ${errorPromedioTotal}`);
    const sumaProporciones = proporciones.reduce((total, proporcion) => total + proporcion, 0);
    const promedioTotal = sumaProporciones / proporciones.length;
    console.log(`Promedio de todas las proporciones: ${promedioTotal}`);
  }

  if (proporcionesDoradas.length === 0) {
    console.log("No se encontraron proporciones que cumplan con la Proporción Dorada en el DOM.");
  } else {
    //console.log(`Promedio de todas las proporciones: ${proporciones}`);
    const sumaProporcionesDoradas = proporcionesDoradas.reduce((total, proporcion) => total + proporcion, 0);
    const promedioDorada = sumaProporcionesDoradas / proporcionesDoradas.length;
    console.log(`Promedio de proporciones que cumplen con la Proporción Dorada: ${promedioDorada}`);
  }
	console.log(`Cantidad de elementos: ${longitudProporciones}`);
	console.log(`Cantidad de elementoss que cumplen con la Proporción Dorada: ${longitudProporcionesDoradas}`);
	console.log(`Proporción de elementos que cumplen con la Proporción Dorada sobre el total: ${longitudProporcionesDoradas/longitudProporciones}`);
}

/*// Llamada para calcular los promedios después de que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
  calcularYMostrarPromedios();
});*/

// Llamada inicial para calcular los promedios después de un retraso
setTimeout(function() {
  calcularYMostrarPromedios();
}, 30); 
