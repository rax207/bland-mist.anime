import webbrowser
import os

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Bland Mist Anime</title>
  <style>
    * {
      box-sizing: border-box;
    }
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background-color: black;
      color: red;
      line-height: 1.6;
    }
    header {
      background-color: red;
      color: black;
      padding: 20px;
      text-align: center;
      font-size: 2em;
      font-weight: bold;
    }
    nav {
      background-color: #1a1a1a;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      padding: 10px;
    }
    nav a {
      color: red;
      text-decoration: none;
      font-weight: bold;
      text-transform: capitalize;
      padding: 8px 16px;
      border-radius: 4px;
      transition: background-color 0.3s, color 0.3s;
    }
    nav a:hover {
      background-color: red;
      color: black;
    }
    .content {
      padding: 20px;
      text-align: center;
    }
    video {
      width: 100%;
      max-width: 600px;
      border: 2px solid red;
      border-radius: 10px;
      margin-top: 20px;
    }
    .anime-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 20px;
      margin-top: 30px;
    }
    .anime-card {
      background-color: #111;
      border: 1px solid red;
      border-radius: 8px;
      padding: 10px;
      text-align: center;
      transition: transform 0.3s, box-shadow 0.3s;
      cursor: pointer;
      color: red;
      text-decoration: none;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .anime-card:hover {
      transform: scale(1.05);
      box-shadow: 0 0 15px red;
      background-color: #220000;
      color: white;
    }
    .anime-card img {
      width: 100%;
      border-radius: 5px;
      height: auto;
      margin-bottom: 10px;
      flex-shrink: 0;
    }
    .anime-card h3 {
      margin: 0;
      font-size: 1rem;
      text-transform: capitalize;
      flex-grow: 1;
    }
    footer {
      background-color: red;
      color: black;
      text-align: center;
      padding: 12px;
      font-size: 0.9rem;
      margin-top: 40px;
    }
  </style>
</head>
<body>

<header>Bland Mist Anime</header>

<nav>
  <a href="#">Home</a>
  <a href="#">Anime List</a>
  <a href="#">Watch</a>
</nav>

<div class="content">
  <h2>🔥 Watch Now</h2>

  <video controls>
    <source src="my-anime.mp4" type="video/mp4" />
    Your browser does not support the video tag.
  </video>

  <h2 style="margin-top: 40px;">✨ Popular Anime</h2>
  <div class="anime-grid">
    <a href="#" class="anime-card" title="Attack on Titan">
      <img src="https://cdn.myanimelist.net/images/anime/10/47347.jpg" alt="Attack on Titan" />
      <h3>Attack on Titan</h3>
    </a>
    <a href="#" class="anime-card" title="Demon Slayer">
      <img src="https://cdn.myanimelist.net/images/anime/1208/94745.jpg" alt="Demon Slayer" />
      <h3>Demon Slayer</h3>
    </a>
    <a href="#" class="anime-card" title="Jujutsu Kaisen">
      <img src="https://cdn.myanimelist.net/images/anime/1160/109947.jpg" alt="Jujutsu Kaisen" />
      <h3>Jujutsu Kaisen</h3>
    </a>
    <a href="#" class="anime-card" title="My Hero Academia">
      <img src="https://cdn.myanimelist.net/images/anime/1575/105763.jpg" alt="My Hero Academia" />
      <h3>My Hero Academia</h3>
    </a>
    <a href="#" class="anime-card" title="Chainsaw Man">
      <img src="https://cdn.myanimelist.net/images/anime/1987/117512.jpg" alt="Chainsaw Man" />
      <h3>Chainsaw Man</h3>
    </a>
    <a href="#" class="anime-card" title="Tokyo Revengers">
      <img src="https://cdn.myanimelist.net/images/anime/1223/126488.jpg" alt="Tokyo Revengers" />
      <h3>Tokyo Revengers</h3>
    </a>
    <a href="#" class="anime-card" title="Spy x Family">
      <img src="https://cdn.myanimelist.net/images/anime/1517/109840.jpg" alt="Spy x Family" />
      <h3>Spy x Family</h3>
    </a>
    <a href="#" class="anime-card" title="One Punch Man">
      <img src="https://cdn.myanimelist.net/images/anime/10/87048.jpg" alt="One Punch Man" />
      <h3>One Punch Man</h3>
    </a>
    <a href="#" class="anime-card" title="Jujutsu Kaisen 2nd Season">
      <img src="https://cdn.myanimelist.net/images/anime/1513/117355.jpg" alt="Jujutsu Kaisen 2nd Season" />
      <h3>Jujutsu Kaisen 2nd Season</h3>
    </a>
  </div>
</div>

<footer>
  &copy; 2025 Bland Mist Anime. Powered by Rifat Souls😎😎😎
</footer>

</body>
</html>
"""

file_name = "bland_mist_anime.html"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(html)

file_path = os.path.abspath(file_name)
webbrowser.open(f"file://{file_path}")

print("✅ Web page created and opened in your browser!")
print("📁 Make sure your anime video is in the same folder as 'my-anime.mp4'")
