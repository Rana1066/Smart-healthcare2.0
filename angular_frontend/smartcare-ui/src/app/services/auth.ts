import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { API_URL } from '../config/api';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root',
})
export class Auth {
  private http = inject(HttpClient);

  apiUrl = 'http://127.0.0.1:8000/api/token/';

  login(username: string, password: string): Observable<any> {
    return this.http.post(this.apiUrl, {
      username,
      password
    });
  }

  saveToken(token: string) {
    localStorage.setItem('access_token', token);
  }

  getToken() {
    return localStorage.getItem('access_token');
  }

  logout() {
    localStorage.removeItem('access_token');
  }
}
