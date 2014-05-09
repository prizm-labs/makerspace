var Form = function(config){

    var formSelector = config.selector;
    var formFields = config.fields;
    var submitUrl = config.submit;

    var submitBtn = $(formSelector).find('[type=submit]')[0];
    var feedbackArea = $(formSelector).find(config.feedback)[0];
    console.log(feedbackArea);

    var l = Ladda.create(submitBtn);

    function bindFormAction() {
        $(formSelector).on('submit',submitForm);
    };

    function unbindFormAction() {
        $(formSelector).off('submit',submitForm);
    };

    function resolveSubmission(response) {
        console.log(response);

        bindFormAction();

        var message;

        if (response.success) {
            message = 'Thanks! Your journey has just begun.';
        } else if (response.data.class=="WebServiceError" && response.data.category=="email") {
            message = 'Please check for your confirmation email';
        } else {
            message = 'Uh oh :( Please try again later';
        }   
        showFeedback(message);
    };

    function showFeedback(message) {
        $(feedbackArea).html(message).fadeIn(300).delay(5000).fadeOut(300);
    }

    function gatherFormData(fields){
        data = {}
        $.each(fields,function(index,field){
            data[field] = $(formSelector).find('[name='+field+']').first().val();
        });
        return data;
    }

    function registrationFormAction() {
        l.start();

        $.ajax({
          method: 'POST',
          url: submitUrl,
          data: gatherFormData(formFields),
          success: resolveSubmission
        }).always(function() { l.stop(); });
        return false;
    };

    function submitForm() {
        event.preventDefault();
        console.log('submitting form');

        // lock out form UI until response
        unbindFormAction();

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
                        feedback: f.feedback,
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


