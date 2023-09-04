playlist_dict = dict()  # intializing a dictionary to store users and there playlist in key value pair


def create_playlist(userList, playList, limit):
    for i in range(len(userList)):
        user_key = userList[i]  # storing username
        play_list = list()  # initialising blank list to store playlist song

        for j in range(len(playList[i])):  # traversing through songs in playlist
            if playList[i][j] in play_list:  # if song is already present in list
                play_list.remove(playList[i][j])  # removing the 1st entry of same data(song)
                play_list.append(playList[i][j])  # inserting data at the end of list
            else:
                play_list.append(playList[i][j])  #
        if len(play_list) > limit:
            play_list = play_list[len(play_list) - limit:]
        playlist_dict[user_key] = play_list

    return playlist_dict


def check_playlist(new_user, new_song, index, playlist_dict=playlist_dict):
    for i in range(len(new_user)):
        if new_user[i] not in playlist_dict:  # checing if user is existing
            play_list = [new_song[i]]
            playlist_dict[new_user[i]] = play_list
        else:
            playlist_dict[new_user[i]].append(new_song[i])
        if len(playlist_dict[new_user[i]]) > index:
            playlist_dict[new_user[i]].pop(0)
    print("new playlist => ", end="")
    print(playlist_dict)

