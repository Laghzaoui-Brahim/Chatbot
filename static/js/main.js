(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Skills
    $('.skill').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 25,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            992:{
                items:2
            }
        }
    });


    // Portfolio isotope and filter
    var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
    });
    $('#portfolio-flters li').on('click', function () {
        $("#portfolio-flters li").removeClass('active');
        $(this).addClass('active');

        portfolioIsotope.isotope({filter: $(this).data('filter')});
    });

  
  /**
   * Navbar links active state on scroll
   */
    
   var sections = document.querySelectorAll("section");

   onscroll = function () {
     var scrollPosition = document.documentElement.scrollTop;
   
     sections.forEach((section) => {
       if (
         scrollPosition >= section.offsetTop - section.offsetHeight * 0.25 &&
         scrollPosition <
           section.offsetTop + section.offsetHeight - section.offsetHeight * 0.25
       ) {
         var currentId = section.attributes.id.value;
         removeAllActiveClasses();
         addActiveClass(currentId);
       }
     });
   };
   
   var removeAllActiveClasses = function () {
     document.querySelectorAll("nav a").forEach((el) => {
       el.classList.remove("active");
     });
   };
   
   var addActiveClass = function (id) {
     // console.log(id);
     var selector = `nav a[href="#${id}"]`;
     document.querySelector(selector).classList.add("active");
   };
   
   var navLinks = document.querySelectorAll("nav a");
   
   navLinks.forEach((link) => {
     link.addEventListener("click", (e) => {
       e.preventDefault();
       var currentId = e.target.attributes.href.value;
       var section = document.querySelector(currentId);
       var sectionPos = section.offsetTop;
       // section.scrollIntoView({
       //   behavior: "smooth",
       // });
   
       window.scroll({
         top: sectionPos,
         behavior: "smooth",
       });
     });
   });  

    
})

(jQuery);

