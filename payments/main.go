// ecommerce_platform/payments/main.go

package main

import (
	"database/sql"
	"encoding/json"
	"net/http"

	_ "github.com/lib/pq"
	"github.com/gorilla/mux"
)

type Payment struct {
	ID        int     `json:"id"`
	OrderID   int     `json:"order_id"`
	Amount    float64 `json:"amount"`
	Status    string  `json:"status"`
}

var db *sql.DB

func main() {
	var err error
	db, err = sql.Open("postgres", "postgres://postgres:12345@db/payments_db?sslmode=disable")
	if err != nil {
		panic(err)
	}

	r := mux.NewRouter()
	r.HandleFunc("/payments", getPayments).Methods("GET")
	r.HandleFunc("/payments/{id}", getPayment).Methods("GET")
	r.HandleFunc("/payments", createPayment).Methods("POST")
	r.HandleFunc("/payments/{id}", updatePayment).Methods("PUT")
	r.HandleFunc("/payments/{id}", deletePayment).Methods("DELETE")

	http.ListenAndServe(":8003", r)
}

func getPayments(w http.ResponseWriter, r *http.Request) {
	rows, err := db.Query("SELECT * FROM payments")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var payments []Payment
	for rows.Next() {
		var payment Payment
		if err := rows.Scan(&payment.ID, &payment.OrderID, &payment.Amount, &payment.Status); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		payments = append(payments, payment)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(payments)
}

func getPayment(w http.ResponseWriter, r *http.Request) {
	id := mux.Vars(r)["id"]
	row := db.QueryRow("SELECT * FROM payments WHERE id = $1", id)

	var payment Payment
	if err := row.Scan(&payment.ID, &payment.OrderID, &payment.Amount, &payment.Status); err != nil {
		if err == sql.ErrNoRows {
			http.Error(w, "Payment not found", http.StatusNotFound)
		} else {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(payment)
}

func createPayment(w http.ResponseWriter, r *http.Request) {
	var payment Payment
	if err := json.NewDecoder(r.Body).Decode(&payment); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	err := db.QueryRow("INSERT INTO payments (order_id, amount, status) VALUES ($1, $2, $3) RETURNING id",
		payment.OrderID, payment.Amount, payment.Status).Scan(&payment.ID)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(payment)
}

func updatePayment(w http.ResponseWriter, r *http.Request) {
	id := mux.Vars(r)["id"]
	var payment Payment
	if err := json.NewDecoder(r.Body).Decode(&payment); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	_, err := db.Exec("UPDATE payments SET order_id = $1, amount = $2, status = $3 WHERE id = $4",
		payment.OrderID, payment.Amount, payment.Status, id)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(payment)
}

func deletePayment(w http.ResponseWriter, r *http.Request) {
	id := mux.Vars(r)["id"]

	_, err := db.Exec("DELETE FROM payments WHERE id = $1", id)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusNoContent)
}
