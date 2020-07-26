

$(function() {
    function submit_message(query) {
 
        $.post( "/query", {
            query: query, 
            
        }, handle_response);
        
        function handle_response(data) {
            // append the bot repsonse to the div
            $('#chat-container').append(`
                <div class="chat-message col-md-5  bot-message">
                    ${data.text}
                </div>
            `).animate({scrollTop: $('#chat-container').prop("scrollHeight")}, 500);
            // remove the loading indicator
            $( "#loading" ).remove();
        }
    }

    $('#target').on('submit', function(e){
        e.preventDefault();
        const query = $('#query').val()
        // return if the user does not enter any text
        if (!query) {
            return
        }
        
        $('#chat-container').append(`
            <div class="chat-message col-md-5 offset-md-7 offset-md-5 human-message">
                ${query}
            </div>
        `).animate({scrollTop: $('#chat-container').prop("scrollHeight")}, 500);
        
        // loading 
        $('#chat-container').append(`
            <div class="chat-message text-center col-md-2  bot-message" id="loading">
                <b>...</b>
            </div>
        `).animate({scrollTop: $('#chat-container').prop("scrollHeight")}, 500);
        
        // clear the text input 
        $('#query').val('')
        
        // send the message
        submit_message(query)
    });
});