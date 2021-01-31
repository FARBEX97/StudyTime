(function ($) {

    $.fn.adjust_BodyMainWrapper_Height = function () {
    
        $(window).bind('load resize', function () {
    
            var viewport_height = $(window).height();
    
            var viewport_width = $(window).width();
    
            var footerHeight = $('.footer_wrapper').height();
    
            var footerTop = $('.footer_wrapper').position().top + footerHeight;
    
            if (footerTop < viewport_height) {
                $('.footer_wrapper').css('margin-top', 10 + (viewport_height - footerTop) + 'px');
            }
    
            $(".navbar-toggle").click(function () {
                if (footerTop < viewport_height) {
                    $('.footer_wrapper').css('margin-top', 10 + (viewport_height - footerTop) + 'px');
                }
            });          
    
        });    
    };
    })(jQuery);