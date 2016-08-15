"""Script to gather IMDB keywords from 2013's top grossing movies."""
import sys

def main():
    """Main entry point for the script."""
    pass

if __name__ == '__main__':
    sys.exit(main())
While it may not look like much, this is a fully functional Python program. You can run it directly and get back the proper return code (0, though to be fair, running an empty file will also return the proper code). Next I'll create stubs for the functions and/or classes that I think I'll need:

"""Script to gather IMDB keywords from 2013's top grossing movies."""
import sys

URL = "http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us,desc&start=1&year=2013,2013"

def main():
    """Main entry point for the script."""
    pass

def get_top_grossing_movie_links(url):
    """Return a list of tuples containing the top grossing movies of 2013 and link to their IMDB
    page."""
    pass

def get_keywords_for_movie(url):
    """Return a list of keywords associated with *movie*."""
    pass

if __name__ == '__main__':
    sys.exit(main())

