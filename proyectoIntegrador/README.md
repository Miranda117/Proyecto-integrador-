itesm-tc1033-a01365726
(la tecla del acento se descompuso)
Dentro de los principales cambios del diagrama anterior con el actual es el cambio de relacion, ya que en la version anterior se mostraba herencia de forma predominante y poca composicion, 
en esta version ocurre justamente lo contrario, se prioriza la relacion de composicion sobre la herencia, cambiando ciertos detalles en la logica, aunque considero que es fundamentalmente similar.

En la nueva version del diagrama es posible notar que todo funciona en torno a AirportAD, la cual curiosamente solo posee metodos, donde cada uno de dichos metodos se encarga de almacenar de forma
relativamente general cierto tipo de informacion, despues de esto, las clases alrededor comienzan la ejecucion de su logica a partir de la lectura de archivo que hizo AirportAD, por esa razon se considero
colocarla en el centro. Las clases con parametros se colocaron en la orilla porque realmente solo indicaban los parametros de los que estaban compuestos, y porque al inicio del programa pueden imaginarse como cajas vacias, 
ya que no tenian asignadas las caracteristicas que anunciaban en forma de parametro.

Se opto por utilizar composicion en vez de herencia debido a la variedad de parametros que podian obtenerse, ya que, a pesar de tener ciertas similitudes, separarlos despues habria sido mas dificil por la diferencia y compresion de los datos en un mismo lugar. La modularidad habria sido un poco menor.



GITHUB REPO: https://github.com/Angel009/itesm-tc1033-a01365726/tree/master/tarea3