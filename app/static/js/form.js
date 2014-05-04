var Form = function(config){

    var formSelector = config.selector;
    var formFields = config.fields;
    var submitUrl = config.submit;

    function bindFormAction() {
        $(formSelector).on('submit',submitForm);
    };

    function unbindFormAction() {
        $(formSelector).off('submit',submitForm);
    };

    function showFormProcessing() {

    };

    function hideFormProcessing() {

    };

    function resolveSubmission(response) {
        console.log(response);

        bindFormAction();
        hideFormProcessing();

        if (response.success) {
            alert('Thanks!');
        } else if (response.data.class=="WebServiceError" && response.data.category=="email") {
            alert('Check for your confirmation email');
        } else {
            alert('Error :( Please try again later');
        }   
    };

    function gatherFormData(fields){
        data = {}
        $.each(fields,function(index,field){
            data[field] = $(formSelector).find('[name='+field+']').first().val();
        });
        return data;
    }

    function registrationFormAction() {

        $.ajax({
          method: 'POST',
          url: submitUrl,
          data: gatherFormData(formFields),
          success: resolveSubmission
        });
    };

    function submitForm() {
        event.preventDefault();
        console.log('submitting form');

        // lock out form UI until response
        unbindFormAction();
        showFormProcessing();

        registrationFormAction();

        return false;
    };

    // form init
    bindFormAction();

    return {
        submit: submitForm
    };
};


var Project = function(config){
    console.log('New Project');
    console.log(config);

    var forms = config.forms;
    
    return {
        bindForms: function() {
            console.log('bindForms');
            console.log(forms);
            $.each(forms,function(index,form) {

                var f = form;

                $(form.selector).each(function(index,formDOM) {
                    console.log(formDOM);
                    console.log(f);

                    var config = {
                        selector: formDOM,
                        submit: f.submit,
                        fields: f.fields
                    };

                    var form = new Form(config);
                    console.log(form);
                });
            });
        }
    };
};


