$(document).ready(function(){
    var fadeout_delay = 5000;
    $('.vote-up').click(function(){
        $.ajax({
            'url': $(this).attr('href'),
            'type': 'POST',
            'dataType': 'json',
            'success': function(data){
                if( data.success ){
                    $('#score-value').text(data.score.score);
                    $('#vote-msg').text('Thanks for Voting!').fadeIn('fast');
                    setTimeout(function(){
                        $('#vote-msg').fadeOut('slow');
                    }, fadeout_delay);
                } else {
                    $('#vote-msg').text(data.error_message).fadeIn('fast');
                    setTimeout(function(){
                        $('#vote-msg').fadeOut('slow')
                    }, fadeout_delay);
                }
            }
            });
        return false;
    });
    $('.vote-down').click(function(){
        $.ajax({
            'url': $(this).attr('href'),
            'type': 'POST',
            'dataType': 'json',
            'success': function(data){
                if( data.success ){
                    $('#score-value').text(data.score.score);
                    $('#vote-msg').text('Thanks for Voting!').fadeIn('fast');
                    setTimeout(function(){
                        $('#vote-msg').fadeOut('slow');
                    }, fadeout_delay);
                } else {
                    $('#vote-msg').text(data.error_message).fadeIn('fast');
                    setTimeout(function(){
                        $('#vote-msg').fadeOut('slow');
                    }, fadeout_delay);
                }
            }
            });
        return false;
    });
});