# TB Progetto di Reti - Politecnico di Milano

Il tb è stato ideato per l'esame dell'anno accademico 2019/2020, ma valido anche per tutti gli anni precedenti.

La memoria RAM fornita nelle specifiche del progetto usa sempre la stessa interfaccia, quindi con buona probabilità il tb sarà utilizzabile anche nei prossimi anni, al peggio apportando qualche modifica.

L'idea alla base è di automatizzare il testing del codice scritto in modo da non dover pensare quali siano i casi necessari per avere una copertura totale.

## Utilizzo

* <b>codice_tb.vhd</b> è il codice del tb.
* <b>Generatore_RAM_2020.py</b> genera molteplici inizializzazioni di valori nella RAM e l'output atteso da ogni singolo test.


I file txt in /data di interesse per il tb
* <b>ram_content.txt</b> su cui itera il tb per leggere i valori di input.
* <b>passati.txt</b> / <b>non_passati.txt</b> scritto dal tb per i risultati dei test.

Il file txt in /data non usato dal tb ma utile per il debugging del codice che si sta testando 
* <b>valori_test.txt</b> contiene l'elenco numerato dei test eseguiti con i valori della RAM e l'output atteso.

### Note
Grazie @davidemerli per aver trovato e sistemato un problema con la parte di test sul doppio start.
