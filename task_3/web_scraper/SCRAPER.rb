require 'nokogiri'
require 'httparty'
require 'byebug' # it is a debugger

# nokogiri , httparty , byebug are the gemfiles required for this project


def scraper  #here we are defining a function as scraper
    url = "https://https://en.wikipedia.org/wiki" #it is the targeted url link
    unparsed_page = HTTParty.get(url) # here we are giving the request to the url here unparsed entity may or may not be the text document
    parsed_page = Nokogiri::HTML(unparsed_page) # using here nokogiri we have parsed the html into the format which we can use to extract data later here parsed entity is the text entity
    
    myarr = Array.new #to call an array and representing it with name of myarr

    mw-body = parsed_page.css('div.content') #here content is the class in a webpage
    
    mw-body.each do |contents|
        body = {
            content = contents.css('p').text #here we are using p for extracting a paragraph from web page
        }

    myarr << body #now appending elements in body in myarr
    end
    myarr.each do |elem|
        puts elem

    end
    byebug #it is a debugging gemfile

    
 
end

scraper # calling a function

