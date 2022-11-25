<h1>Алгоритм Эрли разбора в контекстно-свободной грамматике</h1>
Корневой каталог - task2_earley
<p>Установить нужно pytest, pytest-cov</p>
<div>pip3 install -r requrements.txt</div>
<p>Запуск тестов из корневого каталога (task2_earley):

python3 -m pytest --cov source tests
</p>
<h3> Файлы </h3>
<ol>
<li>grammar - класс контекстно-свободной грамматики</li>
<li>earley - класс алгоритма Эрли </li>
</ol>
В каталоге tests находятся тесты и подкатолог test_files с .gr грамматиками

Файл test2 - пример с семинара

<h3>Формат ввода:</h3>
<ul>
<li>Alphabet: abced</li>

<li>Not terminals: A & B & C & D & S</li>

<li>A -> B & A</li>

<li>S -> a</li>

<li>B -> c</li>

<li>C -> c</li>

<li>A -> a</li>

<li>S -> EPS</li>
</ul>

Где abced - буквы алфавита, A, B, C, D, S - не терминалы, S - стартовая, EPS - пустое слово. Нетерминалы могут быть не однобуквенными. В выводе разделяются &



