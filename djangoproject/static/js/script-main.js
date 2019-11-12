var creacion = true, datos = {};
$('#modalRegistro').on('show.bs.modal', function () {
        if (creacion){
            $('#titulo-reg').text('Nueva tarea');
            $('#id_completado').prop('checked',false);
            $('#id_descripcion').val('');
            $('#boton-reg').text('Guardar');
            $('#forma-registro').attr('action','registrar_item');
        }
        else{
            $('#titulo-reg').text('Editar tarea');
            $('#item_id').val(datos.itemId);
            $('#id_descripcion').val(datos.desc);
            $('#id_completado').prop('checked',datos.completado);
            $('#boton-reg').text('Aceptar');
            $('#forma-registro').attr('action','actualizar_item');
        }
    }
)
$('#modalRegistro').on('shown.bs.modal', function () {
        $('#id_descripcion').trigger('focus');
    }
)

function crear(){
    creacion=true;
}

function editar(descripcion, itemId, completado){
    datos.completado = completado;
    datos.itemId = itemId;
    datos.desc = descripcion;
    creacion=false;
}

function actualizar_checkbox(descripcion, itemId, token){
    var datos = {
        completado: $('#id_compl_lista'+itemId).prop('checked') ? 'True' : 'False',
        item_id: itemId,
        descripcion: descripcion,
        csrfmiddlewaretoken: token
    };   
    $.post("actualizar_item", datos ,function(data){
        location.reload();
    });
}