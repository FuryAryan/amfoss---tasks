
package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	

	"github.com/coreos/pkg/flagutil"
	"github.com/dghubble/go-twitter/twitter"
	"golang.org/x/oauth2"
	"golang.org/x/oauth2/clientcredentials"
)

func main() {
	flags := struct {
		consumerKey    string
		consumerSecret string
	}{}

	flag.StringVar(&flags.consumerKey, "consumer-key", "", "Twitter Consumer Key")
	flag.StringVar(&flags.consumerSecret, "consumer-secret", "", "Twitter Consumer Secret")
	flag.Parse()
	flagutil.SetFlagsFromEnv(flag.CommandLine, "TWITTER")

	if flags.consumerKey == "" || flags.consumerSecret == "" {
		log.Fatal("Application Access Token required")
	}

	// oauth2 configures a client that uses app credentials to keep a fresh token
	config := &clientcredentials.Config{
		ClientID:     flags.consumerKey,
		ClientSecret: flags.consumerSecret,
		TokenURL:     "https://api.twitter.com/oauth2/token",
	}

	// http.Client will automatically authorize Requests
	httpClient := config.Client(oauth2.NoContext)

	// Twitter client
	client := twitter.NewClient(httpClient)


	fmt.Print("Enter First String: ")   
        var first string    
        fmt.Scanln(&first) 

	params := &twitter.UserShowParams{ScreenName: first}
	user, resp, err := client.Users.Show(params)
	_ = resp
	_ = err	

	extra := fmt.Sprintf("%#v",user) //here %#v is a Go-syntax representation of the value

	



    
	f, err := os.Create(first+"test.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	l, err := f.WriteString(extra)
	if err != nil {
		fmt.Println(err)
		f.Close()
		return
	}
	fmt.Println(l, "bytes written successfully")
	err = f.Close()
	if err != nil {
		fmt.Println(err)
			return
	}

	             
    	




	
	


	



}
