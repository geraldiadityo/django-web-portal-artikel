$(document).ready(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:'GET',
            dataType:'JSON',
            beforeSend:function(){
                $('#modal-artikel').modal('show');
            },
            success:function(data){
                $('#modal-artikel .modal-content').html(data.html_form);
            }
        });
    };

    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url:form.attr("action"),
            data:form.serialize(),
            type:'POST',
            dataType:'JSON',
            success:function(data){
                if (data.form_is_valid){
                    alert("data succes sender");
                    $('#artikel-table tbody').html(data.html_artiek_list);
                    $('#modal-artikel').modal('hide');
                }
                else{
                    $('#modal-artikel .modal-content').html(data.html_form);
                }
            }
        });
        return false;
    };

    $('.js-create-artikel').click(loadForm);
    $('#modal-artikel').on('click','.js-artikel-create-form',saveForm);
    $('#artikel-table').on('click','.js-update-artikel',loadForm);
    $('#modal-artikel').on('click','.js-artikel-update-form',saveForm);
    $('#artikel-table').on('click','.js-delete-artikel',loadForm);
    $('#modal-artikel').on('clikc','.js-artikel-delete-form',saveForm);
});