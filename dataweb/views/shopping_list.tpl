<html>
<body>
<h3> Shopping list </h3>
<table>
% for item in shopping_list:
    <tr>

       <td>{{str(item['desc'])}}</td>
       <td><a href="/edit/{{str(item['id'])}}">edit</a></td>
       <td><a href="/delete/{{str(item['id'])}}">delete</a></td>
    </tr>
% end
</table>
<hr/>
</body>
</html>