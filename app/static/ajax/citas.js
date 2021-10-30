function cancelarCita(){

    console.log("Entro funcion formulario")
    var valConfirm = false;

    swal({
        title: "¿Estas seguro de cancelar tu cita?",
        text: "Aun podras seguir visualizando tus citas canceladas en el panel de gestios de citas",
        icon: "warning",
        buttons: { cancel: "Volver",
            catch: {
                text: "Cancelar cita",
                value: true
            },
            defeat: false
        },
        dangerMode: true,
    })
    .then((willDelete) => {
        if (willDelete) {
            valConfirm = true;
            postEliminar();
            
        } 
    });

    

    function postEliminar(){
        $.ajax({
            data : {
                idCita: $('#idCita').val()
            },
            type : 'POST',
            url : '/cancelar_cita'
        })
        .done(function(data){
            console.log("Se recibio una respuesta")
            if(data.error){
                swal("Error: No se pudo cancelar la cita", "error");
                
            }
            else{
                if(data.success){
                    swal("Good!", "Cita cancelada con exito", "success", {button: "Ok"})
                    .then((value) => {
                        if (value) {
                            location.reload()
                        } 
                    });
                    
                }else{
                    swal("No se encontro la cita destino o la cita ya habia sido cancelada con anterioridad", "error");
                }
            }
        });
    }


    function cancelarAccion(){
        swal("La acción se ha cancelado");
    }
    
}