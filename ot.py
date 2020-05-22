import random
from DLP import DLP
from Client import Client
from Server import Server

def main():
    k = int(input("Number of information blocks on server(k) : "))
    e = int(input("Maximum number of channels that can fail (e) : "))
    n = int(input("Total number of channels (n >= k+e) : "))
    data = [random.randint(0, 10000) for i in range(k)]
    print()
    print("Data at Server (randomly generated) : " + str(data))

    dlp = DLP().get_params()
    server = Server(*dlp)
    server.generate_private_key()
    server.generate_public_key()
    server_pub = server.get_public_key()
    print("Server's Public Key: " + str(server_pub))
    client = Client(*dlp)
    client.generate_private_key()
    client.generate_public_key()
    client_pub = client.get_public_key()
    print("Client's Public Key: " + str(client_pub))
    print("Exchanging Public Keys...")
    client.set_partner_public_key(server_pub)
    server.set_partner_public_key(client_pub)
    print("Done")

    print()
    print("CLIENT")
    idx = int(input("Enter index of block to retrieve (<k): "))
    client.set_index(idx)
    Z = client.generate_message_to_server(k)
    print("Message to be sent to server: " + str(Z))
    print("Dividing into n blocks...")
    Z_to_send = client.compute_routing_array(Z, n)
    print("Sending n digitally signed blocks : " + str(Z_to_send))

    print()
    print("SERVER")
    print("Received signed n blocks. Recovering Z...")
    Z_recov = server.recover_array(Z_to_send, k)
    print("Reconstructed Z: " + str(Z_recov))
    if(Z_recov != Z):
        print("Could not recover. Sign has been tampered with.")
        return ;

    print("Decrypting Z...")
    server.decrypt_message(Z_recov)
    print("Sending data blocks to client...")
    to_send = server.send_encrypted_data(data)
    print("k blocks after taking XOR: " + str(to_send))
    signed_to_send = server.compute_routing_array(to_send, n)
    print("Sending digitally signed n blocked data to client: " + str(signed_to_send))

    print()
    print("CLIENT")
    print("Received signed data. Reconstructing...")
    recov_blocks = client.recover_array(signed_to_send, k)
    print("Reconstructed data blocks: " + str(recov_blocks))
    if(recov_blocks != to_send):
        print("Could not recover. Sign has been tampered with.")
        return ;
    print("Extracting " + str(idx) + "th block")
    b = client.extract_block(recov_blocks)
    print("Block value is " + str(b))

    print()
    if b == data[idx]:
        print("Block received is correct!")
    else:
        print("Incorrect data received!")

if __name__=="__main__":
    main()
    
