import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CoreService {
  private baseUrl = 'http://127.0.0.1:8000'

  constructor(private http:HttpClient) { }

  greet():Observable<any>{
    return this.http.get(`${this.baseUrl}/cities`)
  }

  fetchDataPromise(){
    return fetch(`${this.baseUrl}/cities`).then((response)=>{
      if(!response.ok){
        throw new Error('no data found');
      }
      return response.json()
    })
    .then((data)=>{
      return data
    })
  }
}
