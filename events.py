from bs4 import BeautifulSoup
import requests

class Events(object):
	def __init__(self):
		self.r = requests.Session()

	def get(self,id):
		eventR = self.r.get('https://www.nike.com/events-registration/event?id='+str(id))
		eventExtract = eventR.text.encode('utf-8')
		if 'The Ten' in eventExtract:
			bs = BeautifulSoup(eventExtract,'lxml')
			return str(id)+' : THE TEN - '+bs.find(attrs={'property':'og:title'})['content']
		else:
			bs = BeautifulSoup(eventExtract,'lxml')
			return str(id)+' : '+bs.find(attrs={'property':'og:title'})['content']
class main():
	def main():
		start = 87000
		end = 90000

		for i in range(start,end):
			event = Events()
			try:
				events = event.get(i).encode('utf-8')
				if len(events)<=8:
					print str(i)+' : Event not found / access code required'
				else:
					print events

			except:
				print 'Error...'
	if __name__ == '__main__':
		main()