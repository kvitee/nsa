$(document).ready(() => {
  $(".photos-slider").slick({
    slidesToShow: 1,
    arrows: false,
    fade: true,
    asNavFor: ".thumbnails-slider",
  });

  $(".thumbnails-slider").slick({
    mobileFirst: true,
    slidesToShow: 3,
    arrows: false,
    asNavFor: ".photos-slider",
    centerMode: true,
    focusOnSelect: true,
    centerPadding: "15px",
    responsive: [
      {
        breakpoint: 360,
        settings: {
          centerPadding: "30px",
        }
      },
      {
        breakpoint: 432,
        settings: {
          centerPadding: "45px",
        }
      },
      {
        breakpoint: 504,
        settings: {
          centerPadding: "60px",
        }
      },
      {
        breakpoint: 576,
        settings: {
          centerPadding: "0",
          arrows: true,
        }
      },
      {
        breakpoint: 648,
        settings: {
          centerPadding: "0",
          slidesToShow: 5,
          arrows: true,
        }
      },
    ],
  });
});
