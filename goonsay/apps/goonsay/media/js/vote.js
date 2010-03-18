$(document).ready(function(){
    var fadeout_delay = 3000;
    var success_msg = '<div class="vote-msg"><span class="success">Thanks for Voting!</span></div>';
    var error_msg_start = '<div class="vote-msg"><span class="error">';
    var error_msg_end = '</span></div>';

    function voting_handler()
    {
        var voting = $(this).parent();

        voting.find('a').unbind('click');
        voting.find('a').bind('click', function(){ return false; });

        setTimeout(function(){
            voting.find('a').unbind('click');
            voting.find('a').bind('click', voting_handler);
        }, fadeout_delay + 500);

        $.ajax({
            'url': $(this).attr('href'),
            'type': 'POST',
            'dataType': 'json',
            'success': function(data){
                if( data.success ){
                    voting.find('.score-value').text(data.score.score);
                    voting.after(success_msg);
                    voting.parent().find('.vote-msg').fadeIn('slow');
                    setTimeout(function(){
                        voting.parent().find('.vote-msg').fadeOut('slow');
                        voting.parent().find('.vote-msg').remove();
                    }, fadeout_delay);
                } else {
                    voting.after(error_msg_start + data.error_message + error_msg_end);
                    voting.parent().find('.vote-msg').fadeIn('fast');
                    setTimeout(function(){
                        voting.parent().find('.vote-msg').fadeOut('slow');
                        voting.parent().find('.vote-msg').remove();
                    }, fadeout_delay);
                }
            }
            });
        return false;
    }

    $('.vote-link').click(voting_handler);
});
