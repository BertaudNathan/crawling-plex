package main

import (
	"fmt"
	"log"
	"net/http"
	"os/exec"
	"text/template"
)

func SearchHandler(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles("index.html")
	if err != nil {
		panic(err)
	}

	input := r.FormValue("searchinput")
	fmt.Print(input)
	if input != "" {
		cmd := exec.Command("python", "C:/Users/remi_/Desktop/GitLinux/crawling-plex/crawler.py", input)
		out, err := cmd.CombinedOutput()
		if err != nil {
			fmt.Println(err)
		}
		fmt.Println(string(out))
		if err != nil {
			fmt.Fprint(w, err)
		}
	}
	t.Execute(w, nil)
}

func PlexHandler(w http.ResponseWriter, r *http.Request) {
	http.Redirect(w, r, "127.0.0.1:32400", 200)
}

func main() {
	exec.Command("/bin/sh", "-c", "sudo find ...")
	mux := http.NewServeMux()
	http.FileServer(http.Dir("templates"))
	mux.Handle("/template/", http.StripPrefix("/template/", http.FileServer(http.Dir("template"))))
	mux.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))
	mux.Handle("/script/", http.StripPrefix("/script/", http.FileServer(http.Dir("script"))))
	mux.HandleFunc("/", SearchHandler)
	mux.HandleFunc("/plex", PlexHandler)
	fmt.Printf("Serveur http://localhost:8080\n")
	if err := http.ListenAndServe(":8080", mux); err != nil {
		log.Fatal(err)
	}
}
