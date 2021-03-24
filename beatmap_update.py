from requests_html import HTMLSession
import time

def get():
    requests = HTMLSession()
    while True:
        r = requests.get('https://osu.ppy.sh/community/forums/topics/1276374?start=7986628')

        about = r.html.find('[data-post-username="nobreakfast"]')
        count = len(about)
        
        if 'compare' not in locals():
            compare = count
            print('Checking updates')
        else:
            if compare is count:
                print('No updates')
            else:
                print('New Updates')
                return 
        time.sleep(5)   
                
if __name__ == "__main__":
    get()