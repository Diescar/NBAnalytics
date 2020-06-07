$(document).ready(function ()
{
    document.getElementById('#bottom').click(function (e)
    {
        var jump = $(this).attr('href');
        var new_position = $(jump).offset();
        $('html, body').stop().animate({ scrollTop: new_position.top }, 30000);
        e.preventDefault();
    });
});
