# Experimento 01 - Isaí y Camilo

https://proyectofinaluno.atlassian.net/browse/PF-44

EL proposito de este experimento es probar el ASR ```Capacidad de Registro durante Eventos Masivos```

<details>
<summary>Descripcion del ASR</summary>

Como usuario de SportApp cuando me registro en la aplicación , dado que es en operación normal quiero que se pueda realizar el registro en momentos que la aplicación se este usando al mismo tiempo que otras personas. Esto se debe soportar hasta 1000 registros simultáneos. 

<table align="center">
<tr align="center">
<th>ID: PF-44</th>
<th>Escalabilidad</th>
<th>VERSION</th>
<th>V: 01</th>
</tr>
<tr align="center">
<th>FUENTE</th>
<th>ESTIMULO</th>
<th>ARTEFACTO</th>
<th>AMBIENTE</th>
</tr>
<tr align="center">
<td>Usuarios o prueba de estrés</td>
<td>Al evento click del botón registrar</td>
<td>Sistema</td>
<td>	
Operación normal</td>
</tr>
<tr align="center">
<th colspan="2">RESPUESTA</th>
<th colspan="2">MEDIDA DE LA RESPUESTA</th>
</tr>
<tr align="center">
<td colspan="2">El registro del usuario es exitoso</td>
<td colspan="2">Capacidad para soportar hasta 1000 registros simultáneos.</td>
</tr>
</table>

</details>

<details>
<summary>Diagrama implementado para el ASR</summary>


![image](https://github.com/CBarreiro22/experimentosProyectoFInal/assets/111206402/0a75c46e-4f36-4a1a-90e0-9e4d22ba84ff)


</details>

## Estructura de datos para el registro de deportistas

```json
{
    "nombre": "",
    "apellido": "",
    "tipo de identificacion": "CC|ID|PST",
    "edad": 0,
    "peso": 0.0,
    "gender": "M|F",
    "pais de nacimiento": "COL|MEX|BRA",
    "pais de residencia": "COL|MEX|BRA",
    "ciudad de nacimiento": "",
    "ciudad de residencia": "",
    "Antiguedad de residencia": 0,
    "Deportes que practica o desea practicar": "",
}
```


