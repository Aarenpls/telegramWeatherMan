# WeatherMan
<p><b>A simple telegram bot developed at HackNTU 2019</b></p>
<p><b>Try it out on <a href="https://telegram.me/SgWeatherManBot">telegram</a>!</b></p>
<p><b>Server hosted on <a href="https://www.pythonanywhere.com">pythonanywhere</a></b></p>

## What it does
Gives the current weather update (current temperature, UV index, PSI, and area forecast) at 16 specific locations as specified in data.gov.sg to everyone in a group, or directly via private messaging.
<p>These 4 indicators are especially important for social sports group (e.g. water sports, tennis, soccer), even so when there is an increasing trend of social networking platforms centered around sports. However, these 4 arguably most important indicators are located on different pages on NEA's app and website, making it user-unfriendly and annoying.</p>

## How we built it
It is built using Python with <a href="https://github.com/eternnoir/pyTelegramBotAPI">pyTelegramBotAPI</a> and with <a href="https://data.gov.sg/dataset">Singapore's data.gov.sg API</a> for weather updates

## Challenges we ran into
<ol>
<li>Using Python for the first time</li>
<li>Extracting and using the data.gov.sg API (lack of documentation)</li>
</ol>

## Accomplishments that we're proud of
<ol>
<li>Learning Python in 2 hours</li>
<li>Learning how to use pyTelegramBotAPI</li>
<li>Extracting the data from the data.gov.sg API</li>
</ol>

## What we learned
<ol>
<li>Programming in Python!</li>
<li>Roughly how to use the data.gov.sg API</li>
</ol>

## What's next for WeatherMan
<ol>
<li>Instant updates should any of the 4 metrics go beyond the "unhealthy" levels</li>
<li>Letting users geo-tag their location to return the closest station and its data</li>
<li>Options to choose from 2, 6, 12, 24, or 96 hours forecasts</li>
<li>An update button instead of constantly having to give the same commands</li>
</ol>
