<html>
<head>
    <title>Practice Website</title>
    <link rel="stylesheet" href="/static/styles.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <a href="/" class="nav-link active">Home</a>
            <a href="/about" class="nav-link">About</a>
            <a href="/contact" class="nav-link">Contact</a>
        </div>
    </nav>

<!-- Carousel -->
<div id="demo" class="carousel slide" data-bs-ride="carousel">

  <!-- Indicators/dots -->
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#demo" data-bs-slide-to="0" class="active"></button>
    <button type="button" data-bs-target="#demo" data-bs-slide-to="1"></button>
  </div>
  
  <!-- The slideshow/carousel -->
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="static\tomW_holiday.jpg" alt="Los Angeles" class="d-block" style="width:25%">
    </div>
    <div class="carousel-item">
      <img src="static\TowW_prizegiving.jpg" alt="Chicago" class="d-block" style="width:25%">
    </div>
    
  </div>
  
  <!-- Left and right controls/icons -->
  <button class="carousel-control-prev" type="button" data-bs-target="#demo" data-bs-slide="prev">
    <span class="carousel-control-prev-icon"></span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#demo" data-bs-slide="next">
    <span class="carousel-control-next-icon"></span>
  </button>
</div>

<div class="container-fluid mt-3">
    <div class="content-container">
        <div class="media-container">
            <div class="media-image">
              <img src="static\tomW_holiday.jpg" alt="Fun Whangamata vacation" class="media-image">
            </div>
            <div class="media-text">
            <h1>Hello World!</h1>
            <p>My name is Tom Warren. I attend Sacred<br>Heart College. I enjoy computer science<br> and I am in year 11!</p>
            <p>This is a practice website</p>
          </div>
        </div>
    </div>
</body>
</html>