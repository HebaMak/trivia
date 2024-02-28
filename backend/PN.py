
"""
# create a new question
  PN: this command works fine and create question on cmder terminal
      curl -X POST -H "Content-Type: application/json" -d "{\"question\": \"Sample question?\", \"answer\": \"Sample answer\", \"category\": \"1\", \"difficulty\": \"1\"}" http://127.0.0.1:5000/questions
      
  and this command works fine with vscode terminal 
          $body = @{
          question = "Sample question?"
          answer = "Sample answer"
          category = "1"
          difficulty = "1"
      } | ConvertTo-Json

      Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:5000/questions' -ContentType 'application/json' -Body $body
"""





"""
2- # retrieve quizzes
        PN: 
        ** I ussed this curl command on cmder and works
        curl -X POST -H "Content-Type: application/json" -d "{\"previous_questions\":[1,2],\"quiz_category\":{\"id\":1,\"type\":\"Geography\"}}" http://localhost:5000/quizzes
            {
            "question": {
                "answer": "Sample answer",
                "category": "1",
                "difficulty": 1,
                "id": 12,
                "question": "Sample question?"
            },
            "success": true
            }

        
        **I used the help of ChatGPT and  I tried this command in vscode terminal
            $body = @{
                previous_questions = @(1, 2)
                quiz_category = @{
                    id = 1
                    type = "Geography"
                }
            } | ConvertTo-Json

            Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:5000/quizzes' -ContentType 'application/json' -Body $body

            ** it works and the result was: 
            question 
            @{answer=Sample answer; category=1; difficulty=1; id=13; question=Sample question?}    
            
            success  
            True

        ** and this 
            PS C:\Users\lenovo\api_development_and_documentation_project\backend> $headers = @{
            >>     "Content-Type" = "application/json"
            >> }
            >> $body = @{
            >>     previous_questions = @(1, 2)
            >>     quiz_category = @{
            >>         id = 1
            >>         type = "Geography"
            >>     }
            >> } | ConvertTo-Json
            >> 
            >> Invoke-WebRequest -Method POST -Uri 'http://localhost:5000/quizzes' -Headers $headers -Body $body
            >> 


            StatusCode        : 200
            StatusDescription : OK
            Content           : {
                                "question": {
                                    "answer": "Sample answer",
                                    "category": "1",
                                    "difficulty": 1,
                                    "id": 12,
                                    "question": "Sample question?"
                                },
                                "success": true
                                }

            RawContent        : HTTP/1.1 200 OK
                                Access-Control-Allow-Headers: Content-Type, Authorization, true
                                Access-Control-Allow-Methods: GET, POST, PUT, OPTIONS, DELETE
                                Access-Control-Allow-Origin: *
                                Connection: close
                                Cont...
            Forms             : {}
            Headers           : {[Access-Control-Allow-Headers, Content-Type, Authorization, true], [Access-Control-Allow-Methods, GET, POST,     
                                PUT, OPTIONS, DELETE], [Access-Control-Allow-Origin, *], [Connection, close]...}
            Images            : {}
            InputFields       : {}
            Links             : {}
            ParsedHtml        : mshtml.HTMLDocumentClass
            RawContentLength  : 165
"""