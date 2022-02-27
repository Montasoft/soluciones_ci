$(document).ready(function(){
    console.log("archivo userManager.js")
    
    $('#tabla_userManager').Datatable( {

        dom: 'Bfrtip',
        buttons: [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
    });
    ConsultaAjax();
});

let tabla, data;

function ConsultaAjax(){
    $.ajax({
        url: '/ajaxUserManager',
        success: function(response){
            console.log("response", response);
            let responseJson = JSON.parse(response);
            addRowDT(responseJson)
                    
        },
        error:  function(error){
            console.log(error);
        }
    })
};

function addRowDT(data){
    console.log("llegando a AddRowDT")
    console.log(data)
    tabla = $("#tabla_userManager").dataTable();
    for(let i=0; i<data.length; i++){
        if (data[i].Solicitud != null){
            tabla.fnAddData([                
                data[i].nickname,
                data[i].nombre,
                data[i].e-mail,
                data[i].estado,
                '<a href="' + data[i].link + '"/a>Ver'
            ])
        }
    }
}


$(document).on('click', '.btnEditar', function(e){
    let row= ($(this).parent().parent()[0])
    console.log(row)
    data = tabla.fnGetData(row)
    console.log(data)
    fillModalData()

})
function VerSeleccionados(){
// Comprobar los checkbox seleccionados
    let selParaAsignar =[]

    $('input[type=checkbox]:checked').each(function() {
        let row= ($(this).parent().parent()[0]);
        console.log(row);
        data = tabla.fnGetData(row);
        selParaAsignar.push(data[0]);
    })
    console.log(selParaAsignar)
    $("#solicitudSel").val(selParaAsignar);
    CallAsignarOrdenesServer(selParaAsignar)
}
