from flask import request, Response
import requests
from application import app



@app.route('/description', methods = ['POST'])
def description():
    first_sign = request.data.decode('utf-8')
    second_sign = request.data.decode('utf-8')

    #Aries
    if first_sign == 'Aries' and second_sign == 'Aries':
        description = ['50%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Taurus':
        description = ['38%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Gemini':
        description = ['83%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Cancer':
        description = ['42%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Leo':
        description = ['97%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Virgo':
        description = ['63%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Libra':
        description = ['85%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Scorpio':
        description = ['50%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Sagittarius':
        description = ['93%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Capricorn':
        description = ['47%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Aquarius':
        description = ['78%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Pisces':
        description = ['67%']
        return Response(description, mimetype = 'text/plain')

    #Taurus
    elif first_sign == 'Taurus' and second_sign == 'Aries':
        description = ['38%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Taurus' and second_sign == 'Taurus':
        description = ['65%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Taurus' and second_sign == 'Gemini':
        description = ['33%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Taurus' and second_sign == 'Cancer':
        description = ['97%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Taurus' and second_sign == 'Leo':
        description = ['73%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Taurus' and second_sign == 'Virgo':
        description = ['90%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aries' and second_sign == 'Libra':
        description = ['65%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Taurus' and second_sign == 'Scorpio':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Taurus' and second_sign == 'Sagittarius':
        description = ['30%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Taurus' and second_sign == 'Capricorn':
        description = ['98%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Taurus' and second_sign == 'Aquarius':
        description = ['58%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Taurus' and second_sign == 'Pisces':
        description = ['85%']
        return Response(description, mimetype = 'text/plain')

    #Gemini
    elif first_sign == 'Gemini' and second_sign == 'Aries':
        description = ['83%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Gemini' and second_sign == 'Taurus':
        description = ['33%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Gemini' and second_sign == 'Gemini':
        description = ['60%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Gemini' and second_sign == 'Cancer':
        description = ['65%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Gemini' and second_sign == 'Leo':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Gemini' and second_sign == 'Virgo':
        description = ['68%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Gemini' and second_sign == 'Libra':
        description = ['93%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Gemini' and second_sign == 'Scorpio':
        description = ['28%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Gemini' and second_sign == 'Sagittarius':
        description = ['60%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Gemini' and second_sign == 'Capricorn':
        description = ['68%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Gemini' and second_sign == 'Aquarius':
        description = ['85%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Gemini' and second_sign == 'Pisces':
        description = ['53%']
        return Response(description, mimetype = 'text/plain')

    #Cancer
    elif first_sign == 'Cancer' and second_sign == 'Aries':
        description = ['42%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Cancer' and second_sign == 'Taurus':
        description = ['97%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Cancer' and second_sign == 'Gemini':
        description = ['65%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Cancer' and second_sign == 'Cancer':
        description = ['75%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Cancer' and second_sign == 'Leo':
        description = ['35%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Cancer' and second_sign == 'Virgo':
        description = ['90%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Cancer' and second_sign == 'Libra':
        description = ['43%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Cancer' and second_sign == 'Scorpio':
        description = ['94%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Cancer' and second_sign == 'Sagittarius':
        description = ['53%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Cancer' and second_sign == 'Capricorn':
        description = ['83%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Cancer' and second_sign == 'Aquarius':
        description = ['27%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Cancer' and second_sign == 'Pisces':
        description = ['98%']
        return Response(description, mimetype = 'text/plain')


    #Leo
    elif first_sign == 'Leo' and second_sign == 'Aries':
        description = ['97%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Leo' and second_sign == 'Taurus':
        description = ['73%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Leo' and second_sign == 'Gemini':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Leo' and second_sign == 'Cancer':
        description = ['35%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Leo' and second_sign == 'Leo':
        description = ['45%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Leo' and second_sign == 'Virgo':
        description = ['35%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Leo' and second_sign == 'Libra':
        description = ['97%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Leo' and second_sign == 'Scorpio':
        description = ['58%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Leo' and second_sign == 'Sagittarius':
        description = ['93%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Leo' and second_sign == 'Capricorn':
        description = ['35%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Leo' and second_sign == 'Aquarius':
        description = ['68%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Leo' and second_sign == 'Pisces':
        description = ['38%']
        return Response(description, mimetype = 'text/plain')

    #Virgo
    elif first_sign == 'Virgo' and second_sign == 'Aries':
        description = ['63%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Virgo' and second_sign == 'Taurus':
        description = ['90%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Virgo' and second_sign == 'Gemini':
        description = ['68%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Virgo' and second_sign == 'Cancer':
        description = ['90%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Virgo' and second_sign == 'Leo':
        description = ['35%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Virgo' and second_sign == 'Virgo':
        description = ['65%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Virgo' and second_sign == 'Libra':
        description = ['68%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Virgo' and second_sign == 'Scorpio':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Virgo' and second_sign == 'Sagittarius':
        description = ['48%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Virgo' and second_sign == 'Capricorn':
        description = ['95%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Virgo' and second_sign == 'Aquarius':
        description = ['30%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Virgo' and second_sign == 'Pisces':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')


    #Libra
    elif first_sign == 'Libra' and second_sign == 'Aries':
        description = ['85%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Libra' and second_sign == 'Taurus':
        description = ['65%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Libra' and second_sign == 'Gemini':
        description = ['93%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Libra' and second_sign == 'Cancer':
        description = ['43%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Libra' and second_sign == 'Leo':
        description = ['97%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Libra' and second_sign == 'Virgo':
        description = ['68%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Libra' and second_sign == 'Libra':
        description = ['75%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Libra' and second_sign == 'Scorpio':
        description = ['35%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Libra' and second_sign == 'Sagittarius':
        description = ['73%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Libra' and second_sign == 'Capricorn':
        description = ['55%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Libra' and second_sign == 'Aquarius':
        description = ['90%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Libra' and second_sign == 'Pisces':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')


    #Scorpio
    elif first_sign == 'Scorpio' and second_sign == 'Aries':
        description = ['50%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Scorpio' and second_sign == 'Taurus':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Scorpio' and second_sign == 'Gemini':
        description = ['28%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Scorpio' and second_sign == 'Cancer':
        description = ['94%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Scorpio' and second_sign == 'Leo':
        description = ['58%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Scorpio' and second_sign == 'Virgo':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Scorpio' and second_sign == 'Libra':
        description = ['35%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Scorpio' and second_sign == 'Scorpio':
        description = ['80%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Scorpio' and second_sign == 'Sagittarius':
        description = ['28%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Scorpio' and second_sign == 'Capricorn':
        description = ['95%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Scorpio' and second_sign == 'Aquarius':
        description = ['73%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Scorpio' and second_sign == 'Pisces':
        description = ['97%']
        return Response(description, mimetype = 'text/plain')


    #Sagittarius
    elif first_sign == 'Sagittarius' and second_sign == 'Aries':
        description = ['93%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Sagittarius' and second_sign == 'Taurus':
        description = ['30%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Sagittarius' and second_sign == 'Gemini':
        description = ['60%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Sagittarius' and second_sign == 'Cancer':
        description = ['53%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Sagittarius' and second_sign == 'Leo':
        description = ['93%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Sagittarius' and second_sign == 'Virgo':
        description = ['48%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Sagittarius' and second_sign == 'Libra':
        description = ['73%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Sagittarius' and second_sign == 'Scorpio':
        description = ['28%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Sagittarius' and second_sign == 'Sagittarius':
        description = ['45%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Sagittarius' and second_sign == 'Capricorn':
        description = ['60%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Sagittarius' and second_sign == 'Aquarius':
        description = ['90%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Sagittarius' and second_sign == 'Pisces':
        description = ['63%']
        return Response(description, mimetype = 'text/plain')

    #Capricorn
    elif first_sign == 'Capricorn' and second_sign == 'Aries':
        description = ['47%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Capricorn' and second_sign == 'Taurus':
        description = ['98%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Capricorn' and second_sign == 'Gemini':
        description = ['68%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Capricorn' and second_sign == 'Cancer':
        description = ['83%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Capricorn' and second_sign == 'Leo':
        description = ['35%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Capricorn' and second_sign == 'Virgo':
        description = ['95%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Capricorn' and second_sign == 'Libra':
        description = ['55%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Capricorn' and second_sign == 'Scorpio':
        description = ['95%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Capricorn' and second_sign == 'Sagittarius':
        description = ['60%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Capricorn' and second_sign == 'Capricorn':
        description = ['75%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Capricorn' and second_sign == 'Aquarius':
        description = ['68%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Capricorn' and second_sign == 'Pisces':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')

    #Aquarius
    elif first_sign == 'Aquarius' and second_sign == 'Aries':
        description = ['78%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aquarius' and second_sign == 'Taurus':
        description = ['58%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aquarius' and second_sign == 'Gemini':
        description = ['85%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aquarius' and second_sign == 'Cancer':
        description = ['27%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aquarius' and second_sign == 'Leo':
        description = ['68%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aquarius' and second_sign == 'Virgo':
        description = ['30%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aquarius' and second_sign == 'Libra':
        description = ['90%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aquarius' and second_sign == 'Scorpio':
        description = ['73%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aquarius' and second_sign == 'Sagittarius':
        description = ['90%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aquarius' and second_sign == 'Capricorn':
        description = ['68%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aquarius' and second_sign == 'Aquarius':
        description = ['45%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Aquarius' and second_sign == 'Pisces':
        description = ['45%']
        return Response(description, mimetype = 'text/plain')

    #Pisces
    elif first_sign == 'Pisces' and second_sign == 'Aries':
        description = ['67%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Pisces' and second_sign == 'Taurus':
        description = ['85%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Pisces' and second_sign == 'Gemini':
        description = ['53%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Pisces' and second_sign == 'Cancer':
        description = ['98%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Pisces' and second_sign == 'Leo':
        description = ['38%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Pisces' and second_sign == 'Virgo':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Pisces' and second_sign == 'Libra':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Pisces' and second_sign == 'Scorpio':
        description = ['97%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Pisces' and second_sign == 'Sagittarius':
        description = ['63%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Pisces' and second_sign == 'Capricorn':
        description = ['88%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Pisces' and second_sign == 'Aquarius':
        description = ['45%']
        return Response(description, mimetype = 'text/plain')
    elif first_sign == 'Pisces' and second_sign == 'Pisces':
        description = ['60%']
        return Response(description, mimetype = 'text/plain')


