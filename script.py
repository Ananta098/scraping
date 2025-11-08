csv_filename = 'video_data.csv'
# Create a CSV file and write the header row
fieldnames = ['Video URL','Video Title','Video Description']

# Open the CSV file in write mode and write the header
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through each page
    for page_num in range(1, 10):
        # Make a request to the page
        url = f"https://mixkit.co/free-stock-video/nature/?page={page_num}"
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            
            Video_tags = soup.find_all('video', class_='item-grid-video-player__video')
            spans = soup.find_all(class_="item-grid-card__title")
            descriptions = soup.find_all(class_="item-grid-card__description")

# Get the length of the shorter list 
            length = min(len(Video_tags), len(spans), len(descriptions))

# Loop through the shorter list length to avoid IndexError
            for i in range(length):
             video = Video_tags[i]
             span = spans[i]
             desc = descriptions[i]

    # Extract the image URL and title
             video_url = video['src']
             title = span.text
             desc_text = desc.text
                
             video_filename = f"video/{title}.mp4"  # Assuming all images are mp4 format
             with open(video_filename, 'wb') as video_file:
                 video_response = requests.get(video_url)
                 video_file.write(video_response.content)

                
                    
                 writer.writerow({ 'Video URL': video_url,'Video Title':title,'Video Description':desc_text})

            print(f"Page {page_num} processed.")
        else:
            print(f"Failed to retrieve page {page_num}")

print("Scraping and downloading complete.")
