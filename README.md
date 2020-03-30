# TB Progetto di Reti - Politecnico di Milano

Il tb è stato ideato per l'esame dell'anno accademico 2019/2020, ma valido anche per tutti gli anni precedenti.

La memoria RAM fornita nelle specifiche del progetto usa sempre la stessa interfaccia, quindi con buona probabilità il tb sarà utilizzabile anche nei prossimi anni, al peggio apportando qualche modifica.

L'idea alla base è di automatizzare il testing del codice scritto in modo da non dover pensare quali siano i casi necessari per avere una copertura totale. Possono essere generati casualmente ed eseguiti un qualsiasi numero di test.

## File

* <b>codice_tb.vhd</b> è il codice del tb.
* <b>Generatore_RAM_2020.py</b> genera molteplici inizializzazioni di valori nella RAM e l'output atteso da ogni singolo test.


I file txt in /data di interesse per il tb
* <b>ram_content.txt</b> su cui itera il tb per leggere i valori di input.
* <b>passati.txt</b> / <b>non_passati.txt</b> scritto dal tb per i risultati dei test.

Il file txt in /data non usato dal tb ma utile per il debugging del codice che si sta testando 
* <b>valori_test.txt</b> contiene l'elenco numerato dei test eseguiti con i valori della RAM e l'output atteso.

## Utilizzo

Per progetti in anni diversi dal 2019/2020 va riscritto o modificato il generatore in modo da adattarlo alle specifiche.

Nel file codice_tb.vhd leggere la prima riga commentata: vanno cambiati i path dei txt in base a dove si decida di salvarli, sconsiglio di metterli nella directory del progetto perchè potrebbe portare ad avere problemi in lettura. Va bene creare una cartelletta sul Desktop.

Durante la simulazione il tb itera simulando una volta ognuno dei test generati casualmente, legge l'input da ram_content.txt e ne scrive man mano i risultati dividendoli in base all'esito su passati.txt e non_passati.txt.

Una grande quantità di test potrebbe richiedere pochi secondi in simulazione Behavioral e parecchi minuti in simulazione Functional o Timing, garantendo però una copertura praticamente totale dei casi.

### Note
Grazie @davidemerli per aver trovato e sistemato un problema con la parte di test sul doppio start.

Se i prossimi anni qualcuno decidesse di usare il tb e di riadattare il generatore (usando il linguaggio che preferisce) è pregato di mettere i file ram_content.txt a disposizione dei colleghi.
