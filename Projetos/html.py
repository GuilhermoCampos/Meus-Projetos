from os import system

system('cd c:/Users/%USERNAME%/Desktop')
a = open('index.txt', 'w')
b = open('style.txt', 'w')
html = '''<!DOCTYPE html>
<html>
<head>
	<title>Estilizando Tabelas</title>
	<meta chartset="utf-8"/>
	<link rel="stylesheet" type="text/css" href="./style.css"/>
</head>
<body>
	<h2>Estilizando Tabelas</h2>
	<table cellspacing="0">
		<tr>
			<th>Código</th>
			<th>Produto</th>
			<th class="numero">Preço</th>
		</tr>
		<tr class="alternado">
			<td>001</td>
			<td>Notebook</td>
			<td class="numero">R$ 2.500</td>
		</tr>
		<tr>
			<td>002</td>
			<td>Tablet</td>
			<td class="numero">R$ 1.500</td>
		</tr>
		<tr class="alternado">
			<td>003</td>
			<td>Iphone</td>
			<td class="numero">R$ 3.500</td>
		</tr>
		<tr>
			<td>004</td>
			<td>Notebook</td>
			<td class="numero">R$ 3.500</td>
		</tr>
	</table>
</body>
</html>
'''
css = '''
body {
	font-family: "Trebuchet MS", Helvetica, sans-serif;
}

table {
	width: 600px;
	border-collapse: /*collapse*/separate;
	border-spacing:0;
}

th, td {
	padding: 7px;
}

th {
	text-transform: uppercase;
	border-top: 1px solid #999;
	border-bottom: 1px solid #111;
	text-align: left;
	border-collapse: collapse;
	font-size: 90%;
	letter-spacing: 0.1em;
	margin: 0px;
}

tr.alternado {
	background-color: #efefef;
}

tr:hover {
	background-color: #c3e6e5;
}

.numero {
	text-align: right;
}
'''
a.write(html)
b.write(css)
a.close()
b.close()
system('rename index.txt index.html')
system('rename style.txt style.css')
system('start "" "index.html"')
