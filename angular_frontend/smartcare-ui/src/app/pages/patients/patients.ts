import { Component } from '@angular/core';
import { Patient } from '../../services/patient';
import { CommonModule } from '@angular/common';
import { Navbar } from '../../components/navbar/navbar';

@Component({
  selector: 'app-patients',
  imports: [CommonModule,Navbar],
  templateUrl: './patients.html',
  styleUrl: './patients.css',
})
export class Patients {
 patients: any[] = [];

  constructor(
    private patientService: Patient
  ) {}

  ngOnInit(): void {
    this.loadPatients();
  }

  loadPatients() {
    this.patientService.getPatients()
      .subscribe({
        next: (data) => {
          this.patients = data;
        },
        error: (error) => {
          console.log(error);
        }
      });
  }
}
