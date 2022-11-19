<h1>Алгоритм Кока-Янгера-Касами разбора грамматики в НФХ</h1>
Корневой каталог - task2_cyk
<p>Установить нужно pytest, pytest-cov</p>
<div>pip3 install -r requrements.txt</div>
<p>Запуск тестов из корневого каталога (task1):

python3 -m pytest --cov source tests
</p>
<h3> Файлы </h3>
<ol>
<li>grammar - Классы контекстно-свободной грамматики и нормальной формы хомского. Так как разрешили не строить нормальную форму, классы ничем не отличаются.</li>
<li>cyk - класс алгоритма Кока-Янгера-Касами </li>\
</ol>
В каталоге tests находятся тесты и подкатолог test_files с .cnf грамматиками
<ol>
<li>Файлы test1 и test2 различаются выводимостью пустого слова</li>
</ol>

<h3>Формат ввода:</h3>

Alphabet: abced

Not terminals: A & B & C & D & S

Start: S

S -> A & B

A -> B & A

S -> a

B -> c

C -> c

A -> a

S -> EPS


Где abced - буквы алфавита, A, B, C, D, S - не терминалы, S - стартовая, EPS - пустое слово. Нетерминалы могут быть не однобуквенными. В выводе разделяются &


</ul>