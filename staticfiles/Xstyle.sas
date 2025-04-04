// Variables
$primary-color: #000000
$secondary-color: #e7e7e7
$highlight-color: #29a653
$accent-color: #4f9bff
$bg-color: #293541
$card-bg-color: #242c35
$link-color: #8af1ff
$hover-color: #FFD700
$youtube-color: rgb(255, 60, 60)
$youtube-hover-color: rgb(83, 0, 0)
$card-shadow: 0 4px 8px rgba(0, 0, 0, 0.2)
$card-hover-scale: 1.01
$carousel-dark-indicator-active-bg:  $primary-color
$carousel-dark-caption-color:        $primary-color
$carousel-dark-control-icon-filter:  invert(1) grayscale(100)

  
// Mixins
@mixin center-content
  display: flex
  align-items: center
  justify-content: center

@mixin transition($properties...)
  transition: $properties


@mixin card-h5-h2($color) 
    h2
      color: $accent-color
    h5 
      color: $highlight-color
    p
      color: $secondary-color
    

@mixin card-list-header($highlight-color)
    strong
      color: $highlight-color


// Functions
@function get-font-size($size)
  @return $size * 1rem

// Body Styles
body
  background-color: $primary-color !important
  background-size: cover
  margin: 0
  padding-top: 0

// Font Awesome Styling
.fa-solid
  display: block !important

// Section Background
.section-background
  background-image: url('/static/images/Photo+(35+of+41)-min.jpg')
  background-size: cover
  background-position: center
  height: 33vh
  width: 100%
  margin: 0
  padding: 0

li
  color: $secondary-color

// Card Styles
.card
  max-width: 98%
  margin: 0 auto
  padding: .05rem
  border-radius: 8px


// Image Background Styling
#bg-img
  --bs-gutter-x: 0 !important
  padding-right: 0
  padding-left: 0

// Headings
h1, h2
  color: $secondary-color
  text-transform: uppercase
  font-weight: bolder
  vertical-align: middle
  font-family: Poppins, sans-serif

h1
  text-align: center
  margin-top: 5vh
  font-size: get-font-size(2)

h2
  text-align: left
  margin-top: 1vh

h3, h4, p
  color: $secondary-color

// Navbar Brand
.navbar-brand img
  height: 35px !important

// Nav Links
.nav-link
  color: $highlight-color

// Banners
.banners
  @include center-content
  flex-direction: column
  gap: 2px

.banner img
  display: block
  margin: 0 auto
  max-width: 100%

// Card Body
.card-body
  background-color: $bg-color
  color: $secondary-color
  padding-bottom: 10px

p .card-text
  background-color: $card-bg-color
  color: #ffffff !important

// Form Check Labels
.form-check-label
  color: $secondary-color

// Text Centered
.text-center
  background-color: #2b3035
  border-top: none
  margin-top: 10px
  max-width: 90%
  padding: 8px
  border-radius: 8px

// Text Muted
.text-muted
  color: #a7a7a7 !important

// Horizontal Rule
hr
  color: aliceblue

// Small Text
.small-text
  font-size: 0.8em
  color: rgb(176, 176, 176)

// YouTube Icon Styling
.fa-youtube
  font-size: 2rem
  color: $youtube-color
  margin-right: 10px
  @include transition(color 0.3s ease)

.card:hover
  box-shadow: $card-shadow
  transform: scale($card-hover-scale)
  @include transition(0.3s ease-in-out)

.fa-youtube:hover
  color: $youtube-hover-color

// Card Title
.card-title
  color: $accent-color

.container 
    @include card-h5-h2($highlight-color) // Replace #ff6347 with your desired color
  
.row  
@include card-list-header($highlight-color)



// Event Date
.event-date
  font-weight: bold
  color: #aaffaa

// Register Link
.register-link a
  color: $link-color
  text-decoration: none
  font-weight: bold
  &:hover
    color: $hover-color
    text-decoration: underline

// About Us Section
#about_us
  color: #f5f5f5
  background-color: $primary-color


#about-text h4, p
  color: #f5f5f5

// Contact Card
.contact-card
  max-width: 98%
  margin: 0 auto
  padding: 0px
  border-radius: 0

// Logo Styling
.logo-container img
  max-width: 25vh

// Contact Text
.text-container
  color: #f5f5f5

.contact-title a
  font-weight: bold
  font-size: get-font-size(1.2)
  color: #f5f5f5
  text-decoration: none
  &:hover
    text-decoration: underline

.contact-email a,
.contact-location
  color: #f5f5f5
  text-decoration: none

.contact-email a:hover
  text-decoration: underline

// Location Link
.location-link
  color: $link-color
  text-decoration: none
  &:hover
    text-decoration: underline

.fa-location-dot
  font-size: 1.5rem
  color: $highlight-color
  margin-right: 10px
  @include transition(color 0.3s ease)

// Footer Social Icons
.social-icons .fa-solid
  display: inline-block !important

.social-icons a
  text-decoration: none

.social-icons i
  vertical-align: middle

.social-icons .fa-facebook-square
  color: #1877f2 !important

.social-icons .fa-instagram
  color: #e4405f

.social-icons .fa-microphone
  color: #9fc49b

.social-icons .fa-youtube
  color: #ff0000


