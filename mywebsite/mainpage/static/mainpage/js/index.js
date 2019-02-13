$( "document" ).ready(function() {
  "use strict"; // Start of use strict

  // directly shrink if page reloads and its not on the top
  if ($("#mainNav").offset().top > 100) {
    $("#mainNav").css({
      "transition": "padding-top 0s, padding-bottom 0s",
      "-webkit-transition": "padding-top 0s, padding-bottom 0s",
      "-o-transition": "padding-top 0s, padding-bottom 0s",
      "-moz-transition": "padding-top 0s, padding-bottom 0s",
    });
    $("#mainNav .navbar-brand").css({
      "transition": "all 0s",
      "-webkit-transition": "all 0s",
      "-o-transition": "all 0s",
      "-moz-transition": "all 0s",
    });
    $("#mainNav").addClass("navbar-shrink");
  }

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 53) /* default: scrollTop: (target.offset().top - 54) */
      }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    /* target: '#mainNav', */
    target: '#scrollspyNav',
    offset: 56, /* default: 56 */
  });

  // Collapse navbar on scrolls
  var navbarCollapse = function() {
    $("#mainNav").css({
      "transition": "padding-top 0.3s, padding-bottom 0.3s",
      "-webkit-transition": "padding-top 0.3s, padding-bottom 0.3s",
      "-o-transition": "padding-top 0.3s, padding-bottom 0.3s",
      "-moz-transition": "padding-top 0.3s, padding-bottom 0.3s",
    });
    $("#mainNav .navbar-brand").css({
      "transition": "all 0.3s",
      "-webkit-transition": "all 0.3s",
      "-o-transition": "all 0.3s",
      "-moz-transition": "all 0.3s",
    });
    if ($("#mainNav").offset().top < 100) {
      $("#mainNav").removeClass("navbar-shrink");
    } else {
      $("#mainNav").addClass("navbar-shrink");
    }
  };

  var initialScrollEvent = true;
  $(window).scroll(function() {
    console.log("scroll");
    if (!initialScrollEvent) {
      navbarCollapse();
    }
    initialScrollEvent = false;
  });

}); // End of use strict